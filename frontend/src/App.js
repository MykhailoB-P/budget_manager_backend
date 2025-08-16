import React, { useState, useEffect } from 'react';
import Expenses from './Expenses';
import AddExpense from './AddExpense';
import './App.css';

function App() {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/expenses')
      .then(res => res.json())
      .then(data => setExpenses(data));
  }, []);

  const addExpense = (expense) => {
    setExpenses([...expenses, expense]);
  };

  return (
    <div>
      <h1>My First Web App - Budget Manager</h1>
      <AddExpense addExpense={addExpense} />
      <Expenses expenses={expenses} />
    </div>
  );
}

export default App;
