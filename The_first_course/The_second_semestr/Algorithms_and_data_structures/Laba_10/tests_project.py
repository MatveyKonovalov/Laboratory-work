import pytest
from hash_map import Table
from record import Record


class TestSymbolTable:
    """Набор тестов для таблицы символов (вариант 30)"""
    
    @pytest.fixture
    def table(self):
        """Фикстура: создаёт новую таблицу символов"""
        return Table(128)
    
    @pytest.fixture
    def prepared_table(self):
        """Фикстура: таблица с предварительно добавленными данными"""
        st = Table(128)
        
        # Глобальная область
        st.enter_scope("global")
        st.add("global", Record("globalVar1", "int", 10, "global", False, False, 0, ""), False)
        st.add("global", Record("globalVar2", "bool", 11, "global", False, False, 0, ""), False)
        st.add("global", Record("unusedGlobal", "int", 24, "global", False, False, 0, ""), False)
        
        # Область функции
        st.enter_scope("function_calculate")
        st.add("function_calculate", Record("a", "int", 4, "function_calculate", False, False, 0, ""), False)
        st.add("function_calculate", Record("b", "int", 4, "function_calculate", False, False, 0, ""), False)
        st.add("function_calculate", Record("result", "int", 5, "function_calculate", False, False, 0, ""), False)
        st.add("function_calculate", Record("temp", "int", 6, "function_calculate", False, False, 0, ""), False)
        st.add("function_calculate", Record("x", "float", 14, "function_calculate", False, False, 0, ""), False)
        
        # Область блока
        st.enter_scope("block_if")
        st.add("block_if", Record("localVar", "int", 10, "block_if", False, False, 0, ""), False)
        
        return st
    
    # ========== 1. ТЕСТЫ ДОБАВЛЕНИЯ ==========
    
    def test_add_single_variable(self, table):
        """Тест добавления одной переменной"""
        table.enter_scope("global")
        result = table.add("global", Record("x", "int", 10, "global", False, False, 0, ""), False)
        
        assert result == True
        assert table.find("global", "x") is not None
    
    def test_add_multiple_variables(self, prepared_table):
        """Тест добавления нескольких переменных"""
        assert prepared_table.find("global", "globalVar1") is not None
        assert prepared_table.find("global", "globalVar2") is not None
        assert prepared_table.find("function_calculate", "a") is not None
        assert prepared_table.find("function_calculate", "b") is not None
        assert prepared_table.find("block_if", "localVar") is not None
    
    # ========== 2. ТЕСТЫ ОБНАРУЖЕНИЯ ПОВТОРНЫХ ОБЪЯВЛЕНИЙ ==========
    
    def test_redeclaration_detection(self, prepared_table):
        """Тест обнаружения повторного объявления"""
        result = prepared_table.add(
            "function_calculate", 
            Record("x", "float", 14, "function_calculate", False, False, 0, ""), 
            False
        )
        assert result == False
    
    def test_redeclaration_different_scopes(self, table):
        """Разные области - не считается повторением"""
        table.enter_scope("scope1")
        table.add("scope1", Record("x", "int", 10, "scope1", False, False, 0, ""), False)
        
        table.enter_scope("scope2")
        result = table.add("scope2", Record("x", "float", 20, "scope2", False, False, 0, ""), False)
        
        assert result == True
        assert table.find("scope1", "x") is not None
        assert table.find("scope2", "x") is not None
    
    # ========== 3. ТЕСТЫ ПОИСКА ==========
    
    def test_lookup_current_scope(self, prepared_table):
        """Поиск в текущей области"""
        current = prepared_table.current_scope()
        assert current == "block_if"
        
        found = prepared_table.find(current, "localVar")
        assert found is not None
        assert found.name == "localVar"
    
    def test_lookup_parent_scope_not_found(self, prepared_table):
        """Поиск переменной из родительской области в текущей - не найдена"""
        current = prepared_table.current_scope()
        assert current == "block_if"
        
        not_found = prepared_table.find(current, "result")
        assert not_found is None
    
    # ========== 4. ТЕСТЫ РЕКУРСИВНОГО ПОИСКА ==========
    
    def test_recursive_lookup_finds_parent_variable(self, prepared_table):
        """Рекурсивный поиск находит переменную в родительской области"""
        found = prepared_table.find_recursive("result")
        assert found is not None
        assert found.name == "result"
        assert found.scope == "function_calculate"
    
    def test_recursive_lookup_finds_global_variable(self, prepared_table):
        """Рекурсивный поиск находит глобальную переменную"""
        found = prepared_table.find_recursive("globalVar1")
        assert found is not None
        assert found.name == "globalVar1"
        assert found.scope == "global"
    
    def test_recursive_lookup_not_found(self, table):
        """Рекурсивный поиск несуществующей переменной"""
        table.enter_scope("global")
        found = table.find_recursive("nonexistent")
        assert found is None
    
    # ========== 5. ТЕСТЫ ОБНОВЛЕНИЯ ФЛАГА ИСПОЛЬЗОВАНИЯ ==========
    
    def test_change_use_flag(self, prepared_table):
        """Тест изменения флага использования"""
        var_before = prepared_table.find("function_calculate", "result")
        assert var_before.used == False
        
        prepared_table.change_use_in("function_calculate", "result")
        
        var_after = prepared_table.find("function_calculate", "result")
        assert var_after.used == True
    
    def test_change_use_flag_nonexistent(self, table, capsys):
        """Изменение флага для несуществующей переменной"""
        table.enter_scope("global")
        table.change_use_in("global", "nonexistent")
        captured = capsys.readouterr()
        assert "Exception: var 'nonexistent' not in node" in captured.out
    
    # ========== 6. ТЕСТЫ НЕИСПОЛЬЗУЕМЫХ ИДЕНТИФИКАТОРОВ ==========
    
    
    
    def test_get_unused_global(self, prepared_table):
        """Получение неиспользуемых глобальных переменных"""
        unused = prepared_table.get_no_use_in("global")
        unused_names = [r.name for r in unused]
        
        assert "globalVar2" in unused_names
        assert "unusedGlobal" in unused_names
    
   
    
    def test_delete_zone(self, prepared_table):
        """Тест удаления области видимости"""
        # Проверяем, что переменная существует
        assert prepared_table.find("block_if", "localVar") is not None
        
        # Удаляем область
        prepared_table.delete_zone("block_if")
        
        # Проверяем, что переменная удалена
        assert prepared_table.find("block_if", "localVar") is None
    
    def test_delete_zone_updates_capacity(self, prepared_table):
        """Удаление области корректно обновляет capacity"""
        capacity_before = prepared_table.capacity
        
        # В области block_if 1 переменная
        prepared_table.delete_zone("block_if")
        
        capacity_after = prepared_table.capacity
        assert capacity_after == capacity_before - 1
    
    def test_exit_scope_removes_variables(self, table):
        """Выход из области через стек удаляет все переменные"""
        table.enter_scope("outer")
        table.add("outer", Record("outer_var", "int", 5, "outer", False, False, 0, ""), False)
        
        table.enter_scope("inner")
        table.add("inner", Record("inner_var", "int", 10, "inner", False, False, 0, ""), False)
        
        # Проверяем, что переменные существуют
        assert table.find("inner", "inner_var") is not None
        assert table.find("outer", "outer_var") is not None
        
        # Выходим из inner
        table.exit_scope()
        
        # Переменная inner должна быть удалена
        assert table.find("inner", "inner_var") is None
        # Переменная outer должна остаться
        assert table.find("outer", "outer_var") is not None
    
    def test_delete_var(self, prepared_table):
        """Удаление отдельной переменной"""
        assert prepared_table.find("function_calculate", "temp") is not None
        
        prepared_table.delete_var("function_calculate", "temp")
        
        assert prepared_table.find("function_calculate", "temp") is None
    
    # ========== 8. ТЕСТЫ СТЕКА ОБЛАСТЕЙ ==========
    
    def test_scope_stack_order(self, table):
        """Проверка порядка стека областей"""
        table.enter_scope("global")
        table.enter_scope("function")
        table.enter_scope("block")
        
        assert table.current_scope() == "block"
        
        table.exit_scope()
        assert table.current_scope() == "function"
        
        table.exit_scope()
        assert table.current_scope() == "global"
    
    def test_current_scope_empty(self, table):
        """Пустой стек областей"""
        assert table.current_scope() is None
    
    # ========== 9. ТЕСТЫ ГРАНИЧНЫХ СЛУЧАЕВ ==========
    
    def test_add_to_nonexistent_scope(self, table):
        """Добавление в несуществующую область"""
        table.enter_scope("global")
        result = table.add("nonexistent", Record("x", "int", 10, "nonexistent", False, False, 0, ""), False)
        assert result == True
        assert table.find("nonexistent", "x") is not None
    
    def test_find_in_nonexistent_scope(self, table):
        """Поиск в несуществующей области"""
        result = table.find("nonexistent", "x")
        assert result is None
    
    def test_get_no_use_in_nonexistent_scope(self, table):
        """Получение неиспользуемых из несуществующей области"""
        result = table.get_no_use_in("nonexistent")
        assert result == []
    
    # ========== 10. ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ ==========
    
    def test_large_number_of_variables(self, table):
        """Тест на большое количество переменных (10,000)"""
        table.enter_scope("large")
        
        for i in range(10000):
            record = Record(f"var_{i}", "int", i, "large", False, False, 0, "")
            table.add("large", record, False)
        
        
        # Проверяем несколько случайных переменных
        assert table.find("large", "var_0") is not None
        assert table.find("large", "var_5000") is not None
        assert table.find("large", "var_9999") is not None
    
    def test_recursive_lookup_performance(self, table):
        """Производительность рекурсивного поиска"""
        # Создаём глубокую вложенность
        table.enter_scope("level0")
        table.add("level0", Record("target", "int", 0, "level0", False, False, 0, ""), False)
        
        for i in range(1, 100):
            table.enter_scope(f"level{i}")
            table.add(f"level{i}", Record(f"var_{i}", "int", i, f"level{i}", False, False, 0, ""), False)
        
        # Ищем переменную на самом глубоком уровне вложенности
        found = table.find_recursive("target")
        assert found is not None
        assert found.name == "target"


# ========== ЗАПУСК ТЕСТОВ ==========
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])