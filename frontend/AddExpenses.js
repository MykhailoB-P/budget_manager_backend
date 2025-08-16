import React, { useState } from 'react';

function AddExpense({ addExpense }) {
    const [amount, setAmount] = useState('');
    const [category, setCategory] = useState('');
  
    const handleSubmit = (e) => {
      e.preventDefault();
      fetch('http://127.0.0.1:5000/expenses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount, category })
      })
      .then(res => res.json())
      .then(data => {
        addExpense(data);
        setAmount('');
        setCategory('');
      });
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input 
          type="number" 
          placeholder="Amount" 
          value={amount} 
          onChange={(e) => setAmount(e.target.value)} 
          required 
        />
        <input 
          type="text" 
          placeholder="Category" 
          value={category} 
          onChange={(e) => setCategory(e.target.value)} 
          required 
        />
        <button type="submit">Add Expense</button>
      </form>
    );
  }
  
  export default AddExpense;