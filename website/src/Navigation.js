import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  const [tests, setTests] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:5000/tests').then((response) => {
      setTests(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Test List</h2>
      <table>
        <thead>
          <tr>
            <th>Test Name</th>
            <th>Date Created</th>
            <th>Last Run Status</th>
          </tr>
        </thead>
        <tbody>
          {tests.map((test) => (
            <tr key={test.id}>
              <td>{test.name}</td>
              <td>{test.date_created}</td>
              <td>{test.last_run_status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
export default Navigation;
