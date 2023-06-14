import './App.css';
import './style.css'
import {useState} from 'react';
import { useEffect } from 'react';
import axios from 'axios';
import Swal from 'sweetalert2';
import Modal from 'react-modal'
import {Link} from 'react-router-dom'


function TestListModal(props) {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  function openModal() {
    setModalIsOpen(true);
  }

  function closeModal() {
    setModalIsOpen(false);
  }

  return (
    <div>
      <button onClick={openModal}>Show Created Test</button>
      <Modal isOpen={modalIsOpen} onRequestClose={closeModal}>
        <h2>List of Test Names</h2>
        <ul>
          {props.testNames.map((name, index) => (
            <li key={index}>{name}</li>
          ))}
        </ul>
        <button onClick={closeModal}>Close</button>
      </Modal>
    </div>
  );
}



function Child(props) {
  const [action, setAction] = useState('');
  const [tag, setTag] = useState('');
  const [description, setDescription] = useState('');
  const [value, setValue] = useState('');
  const [valueLabel, setValueLabel] = useState('Value');


  const handleActionChange = (e) => {
    setAction(e.target.value);
    if(e.target.value === "type"){
      setValueLabel('Content to Type');
    }
    else{
      setValueLabel('Value');
    }
  };

  const handleTagChange = (e) => {
    setTag(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleValueChange = (e) => {
    setValue(e.target.value);
  };

  let sentence = `Perform ${action} action on ${tag} with the description "${description}"`;

  if (tag === 'input' && action !== 'check') {
    sentence += ` and send the value "${value}"`;
  } else if (action === 'check') {
    sentence = `Check if the element with tag ${tag} and description : "  ${description} "  is equal to ${value}`;
  }

useEffect(() => {
    const childData = {
      tag: tag,
      action: action,
      description : description,
      value : value
    };
    props.onDataChange(props.id,childData);
  }, [tag, action , description , value]);

  return (
    <div className='sentence-base'>
      <div>
        <label htmlFor="action">Action:</label>
        <select id="action" onChange={handleActionChange}>
          <option value="">Select an action</option>
          <option value="click">Click</option>
          <option value="type">Type</option>
          <option value="Hover">Hover Over</option>
          <option value="check">Check if</option>
        </select>
      </div>
      <div>
        <label htmlFor="tag">Tag:</label>
        <select className= "select" id="tag" onChange={handleTagChange}>
          <option value="">Select a tag</option>
          <option value="button">button</option>
          <option value="link">link</option>
          <option value="input">input</option>
          <option value="span">span</option>
        </select>
      </div>
      <div>
        <label htmlFor="description">Additional description:</label>
        <input type="text" id="description" onChange={handleDescriptionChange} />
      </div>
        <div>
          <label htmlFor="value"> {valueLabel}:</label>
          <input type="text" id="value" onChange={handleValueChange} />
        </div>
      <div>{sentence}</div>
    </div>
  );
};


function Home() {
  const [data, setData] = useState([]);
  const [children, setChildren] = useState([])
  const [websiteUrl, setWebsiteUrl] = useState('')
  const [testName, setTestName] = useState('')
  
  const [testNames, setTestNames] = useState(['Test 1', 'Test 2', 'Test 3']);
  const url = "http://localhost:5000/create-test/"



  

  function setUrl(event){
    setWebsiteUrl(event.target.value);
  }
  function setTest(event){
    setTestName(event.target.value)
  }
  function collectInfo(){
    const payload = {
      "base_url":websiteUrl,
      "test_name":testName,
      "sentences" : data.map(x=>x["payload"])
    }
    console.log(data)
    axios.post(url, payload).then((resp) => {
      console.log(resp);
      if (resp.status === 200) {
        Swal.fire({
          icon: 'success',
          title: `Test Created Successfully under the name ${testName}`,
          showConfirmButton: false,
          timer: 1500,
        });
      }
    });
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
        <div className = "main-section">
        <h1 name="createSentence"> Create Test</h1>

      {/*
        Render child components and pass onDataChange function as prop.
        This allows the child components to send their data to the parent component.
      */}
      <input placeholder="Test Name" onChange={setTest}></input>
      <input placeholder = "Website URL" onChange={setUrl}></input>
      <button onClick={collectInfo}>Finish</button>
      <button onClick= {addChild}> Add Sentence</button>
      <button><Link to="/tests"> Tests</Link></button>


      </div>
      {children}

      {/* Button to collect data from child components */}

 

      {/* Return list of data objects collected from child components */}
    </div>
  );
}


export default Home;