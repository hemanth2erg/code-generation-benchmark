import React from 'react';

function App() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">LLM Debugger</h1>
      <p>Paste a response below to analyze:</p>
      <textarea className="border w-full mt-2 p-2" rows="10" />
    </div>
  );
}

export default App;
