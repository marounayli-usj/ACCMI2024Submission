import './App.css';
import './style.css'
import {useState} from 'react';
import { useEffect } from 'react';
import axios from 'axios';
// const  Sentence =  ({onCollectData}) => {

//   const [action, setAction] = useState('')
//   const [description, setDescription] = useState('')
//   const [tag, setTag] = useState('')
//   const [value, setValue] = useState('')
//   const [transition, setTransition] = useState('')
//   const [placeholderInput, setPlaceholderInput] = useState('Enter value')
//   function inputValue(event){
//     setValue(event.target.value);
//   }
//   function selectTag(event){
//     const selected = event.target.value;
//     if(selected == 'input'){
//       setTransition('with placeholder');
//       setPlaceholderInput('Enter Placeholder');
//     }
//     else{
//       setTransition('with value');
//       setPlaceholderInput('Enter Value');
//     }
//     setTag(event.target.value);
//   }

//   function selectAction(event){
//     setAction(event.target.value);
//   }

//   function inputDescription(event){
//     setDescription(event.target.value);
//   }

//   function onCollectData(){
//     return {"action" : action , "tag" : tag}
//   }


//   return (<div className = "sentence-base">
//   <div>
//   <h1 name="createSentence"> Create sentence</h1>

//   <select onChange = {selectAction}>
//     <option value="">-- Select an action --</option>
//     <option value="Click on the ">Click</option>
//     <option value="Hover over">Hover over</option>
//     <option value="Type">Type</option>
//   </select>
//   <select onChange = {selectTag}>
//     <option value="">Select a tag</option>
//     <option value="Button">Button</option>
//     <option value="Link">Link</option>
//     <option value="Span">Span</option>
//     <option value="DropDown">DropDown</option>
//     <option value= "input"> Input</option>
//   </select>
//   <input type='text' placeholder='Enter element description' onChange = {inputDescription}/>
//   <input type='text' placeholder={placeholderInput} onChange = {inputValue}/>

// </div>

// <label>Generated sentence: " {action} {description} {tag} {transition} {value}" </label>

//   </div>);
// }
// function App() {

//   const [sentences, setSentences] = useState([]);
//   const [test, setTest] = useState([])

//   const addSentences = () => {
//     setSentences([...sentences, <Sentence key={sentences.length} onDataChange={handleData} className="child-component"/>]) ;
//   };

//   function handleData(childData){
  
//     setTest(prevData=> [...prevData , childData])
//   }
//   const createTest = () => {
//     const newData = [];
//     const childComponents = document.querySelectorAll('.child-component');
//     childComponents.forEach((component) => {
//       newData.push(component.childData);
//     });
//     setTest(newData)
//     console.log(test)
//   }

//   return (
//     <div className="App">
//       {sentences}
//       <button className= "add-sentence" onClick={addSentences}> Add actions </button>
//       <button onClick={createTest}>Create Test</button>
//     </div>
//   );
// }

// export default App;



// Child component
function Child(props) {
  const [tag, setTag] = useState('');
  const [action, setAction] = useState('');
  const [description, setDescription] = useState('');


  useEffect(() => {
    const childData = {
      tag: tag,
      action: action,
    };
    props.onDataChange(props.id,childData);
  }, [tag, action]);
  return (
    <div>
      <input value={tag} onChange={(e) => setTag(e.target.value)} placeholder="Tag" />
      <input value={action} onChange={(e) => setAction(e.target.value)} placeholder="Action" />
    </div>
  );

  
}

// Parent component
function App() {
  const [data, setData] = useState([]);
  const [children, setChildren] = useState([])

  function collectInfo(){
    console.log(data);
  }
  // Collect data from child components
  

  function handleData(index,payload){
    const newdata=  [...data];
    newdata[index]= {...newdata[index],payload};
    setData(newdata)
}
  function addChild(){
    setData(data.length==0 ? [{},]:[...data,{}])
    setChildren(c =>{
    if(c.length==0){
      return [<Child key={0} id={0} onDataChange= {handleData}/>];
    }
    else{
    return [...children, <Child key={children.length} id= {children.length}  onDataChange={handleData} />]
    }
  })
}
  // Render parent component
  return (
  
    <div>
      <button onClick= {addChild}> Add child</button>
      {/*
        Render child components and pass onDataChange function as prop.
        This allows the child components to send their data to the parent component.
      */}
      {children}

      {/* Button to collect data from child components */}
      <button onClick={collectInfo}>Collect Data</button>

      {/* Return list of data objects collected from child components */}
    </div>
  );
}

export default App;