import React from 'react';

function Expenses({ expenses }) {
    return (
      <div>
        <h2>Expenses List</h2>
        <ul>
          {expenses.map((e, index) => (
            <li key={index}>
              {e.category}: ${e.amount} on {e.date}
            </li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default Expenses;