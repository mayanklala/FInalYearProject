import './App.css';
import React from 'react';
import {Button} from './Components/Button';
function App() {
  return (
    <div>
    <div className="App">
    <h1>
      Plagiarism detector for handwritten documents
    </h1>
    </div>
    
    <Button 
    type="button"
    buttonStyle="btn--upload--outline">Hello</Button>
    
    </div>
  );
}

export default App;
