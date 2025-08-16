import React, { useState, useEffect } from 'react';
import Expenses from './Expenses';
import AddExpense from './AddExpense';
import './App.css'; // Make sure to import CSS for animations

function App() {
  const [expenses, setExpenses] = useState([]);
  const [showExpenses, setShowExpenses] = useState(false);

  useEffect(() => {
    // Fetch expenses from backend
    fetch('http://127.0.0.1:5000/expenses')
      .then(res => res.json())
      .then(data => setExpenses(data))
      .catch(err => console.error('Error fetching expenses:', err));
  }, []);

  const addExpense = (expense) => {
    setExpenses([...expenses, expense]);
  };

  const toggleExpenses = () => {
    setShowExpenses(!showExpenses);
  };

  return (
    <div className="App">
      <h1>My First Web App - Budget Manager</h1>
      <AddExpense addExpense={addExpense} />

      <button onClick={toggleExpenses}>
        {showExpenses ? 'Hide list' : 'Show list'}
      </button>

      <div className={`expenses-container ${showExpenses ? 'show' : 'hide'}`}>
        {showExpenses && <Expenses expenses={expenses} />}
      </div>
    </div>
  );
}

export default App;
