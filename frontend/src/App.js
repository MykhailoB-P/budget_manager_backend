import React, { useState, useEffect } from 'react';
import Expenses from './Expenses';
import AddExpense from './AddExpense';
import './App.css';

function App() {
  const [expenses, setExpenses] = useState([]);
  const [showExpenses, setShowExpenses] = useState(false); // новый стейт для показа/скрыти

  // Function for loading expenses from database
  useEffect(() => {
    fetch('http://127.0.0.1:5000/expenses')
      .then(res => res.json())
      .then(data => setExpenses(data));
  }, []);

  const addExpense = (expense) => {
    setExpenses([...expenses, expense]);
  };

  const toggleExpenses = () => {
    setShowExpenses(!showExpenses);
  };

  return (
    <div>
      <h1>My First Web App - Budget Manager</h1>
      <AddExpense addExpense={addExpense} />

      <button onClick={toggleExpenses}>
        {showExpenses ? 'Hide list' : 'Show List'}
      </button>

      {showExpenses && <Expenses expenses={expenses} />}
    </div>
  );
}

export default App;
