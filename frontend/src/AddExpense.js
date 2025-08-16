import React, { useState } from 'react';

function AddExpense({ addExpense }) {
    const [amount, setAmount] = useState('');
    const [category, setCategory] = useState('');


    //categories
    
    const categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"];

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

        <select value={category} onChange={(e) => setCategory(e.target.value)} required>
        {categories.map((cat, index) => (
          <option key={index} value={cat}>{cat}</option>
        ))}
      </select>

        <button type="submit">Add Expense</button>
      </form>
    );
  }
  
  export default AddExpense;