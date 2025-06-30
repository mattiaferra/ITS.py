import React, { useState } from 'react';

const Contatore = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount((oldCount) => {
      if (oldCount < 4) {
        return oldCount + 1;
      } else {
        return oldCount;
      }
    });
  };

  const decrement = () => {
    setCount(count - 1);
  };

  return (
    <>
      <div>{count}</div>
      <div>
        <button onClick={decrement}>Decrementa</button>&nbsp;
        <button onClick={increment}>Incrementa</button>
      </div>
    </>
  );
};

export default Contatore;
