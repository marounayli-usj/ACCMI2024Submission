import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import io from 'socket.io-client'
import './tables.css';
import Swal from 'sweetalert2'
function WebTestsComponent() {

  const [screenshots,setScreenshots] = useState([])

  useEffect(() => {
    const socket = io('http://localhost:5555'); // Replace with your server URL
    socket.on('connect', () => {
      console.log('Connected to server');
      socket.emit('hello');
    });
    socket.on('images', (msg) => {
      setScreenshots(screenshots => [...screenshots, msg["data"]]);
    });
    return () => {
      socket.disconnect();
    };
  }, []);


    function handleRunTest(id) {

      Swal.fire({
        title: 'Test is running!',
        text: 'Please wait while we run the test...',
        icon: 'success',
        timerProgressBar: true,
        showConfirmButton: true,
        timer: 10000
      });

        axios.post('http://localhost:5000/run-test', { "id":id })
          .then(response => {
            console.log(response.data);
          })
          .catch(error => {
            console.error(error);
          });
      }


    const [tests, setTests] = useState([]);

    useEffect(() => {
      axios.get('http://localhost:5000/tests').then((response) => {
        setTests(response.data);
      });
    }, []);
  
        return (
            <div>
            <div className = "web-tests">
            <h2>Test List</h2>
            <table className="">
              <thead>
                <tr>
                  <th>Test Name</th>
                  <th>Date Created</th>
                  <th>Last Run Status</th>
                </tr>
              </thead>
              <tbody>
              {tests.map((testObject) => {
            const testId = Object.keys(testObject)[0];
            const test = testObject[testId];
            return (
              <tr key={testId}>
                <td>{test.test_name}</td>
                <td>{test.date_created}</td>
                <td>{test.last_run_status}</td>
                <td>
                  <button onClick={()=>handleRunTest(testId)}> Run Test
                  </button>
                </td>
                
              </tr>
            );
          })}
              </tbody>
            </table>
          </div>

            <div>
        {screenshots.map((image, index) => (
          <div>
        <img key={index} src={`data:image/png;base64,${image}`} alt={`Screenshot ${index}`} />
        </div>
      ))}
      </div>
          </div>
        );
}

export default WebTestsComponent;
