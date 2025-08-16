import './App.css';
import React from 'react';

function Expenses({ expenses }) {
    if (!expenses.length) return <p>No expenses to show.</p>;

    return (
      <div>
        <h2>Expenses List</h2>
        <ul>
          {expenses.map((e, index) => (
            <li key={index}>
              {e.category}: ${e.amount} on {e.date || "Unknown date"}
            </li>
          ))}
        </ul>
      </div>
    );
}

export default Expenses;
