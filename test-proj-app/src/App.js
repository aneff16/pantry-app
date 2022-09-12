import {useState, useEffect} from 'react';
import './App.css';
import { getPantry, addPantryItem, editPantryItem, deletePantryItem } from './Requests';

function App() {
  const [newItem, setNewItem] = useState({});
  const [pantry, setPantry] = useState([]);

  const getData = async () => {
    const res = await getPantry();
    setPantry(res);
  };

  const handleChange = ({target}) => {
    // put this in if you want form to create the item id: id: Date.now()
    setNewItem((prev) => ({...prev, [target.name]: target.value}));
  };

  const addItem = async item => {
    let found = false;
    for (let i = 0; i < pantry.length; i++) {
      if (item.name === pantry[i].name) {
        pantry[i].quantity = parseInt(pantry[i].quantity) + parseInt(item.quantity);
        await editPantryItem(pantry[i]);
        found = true;
        break;
      }
    }
    if (!found){
      await addPantryItem(item);
      setPantry((prev) => ([...prev, item]));
    }
  };

  const handleAdd = async item => {
    item.quantity++;
    await editPantryItem(item);
    setPantry([...pantry]);
  };

  const handleSubtract = async item => {
    if (item.quantity === 1) {
      setPantry((prev) => prev.filter(
        (p) => p.name !== item.name
      ));
      await deletePantryItem(item.id);
    }else {
      item.quantity--;
      await editPantryItem(item);
      setPantry([...pantry]);
    }
  };

  const handleDelete = async id => {
    setPantry((prev) => prev.filter(
      (p) => p.id !== id
    ));
    await deletePantryItem(id);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!newItem.quantity || !newItem.name) {
      return;
    }else {
      addItem(newItem);
      setNewItem({});
    }
    event.target.reset();
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <h1>Add an item to your pantry: </h1>
      <form onSubmit={handleSubmit}>
        <label>
          Item:
          <input type='text' name='name' onChange={handleChange} onInput={handleChange} value={newItem.name} />
        </label>
        <br />
        <label>
          Quantity:
          <input type='number' name='quantity' onChange={handleChange} onInput={handleChange} value={newItem.quantity} />
        </label>
        <br />
        <input type='submit' value='Submit' />
      </form>
      <div>Item: {newItem.name}</div>
      <div>Quantity: {newItem.quantity}</div>
      <div>ID: {newItem.id}</div>
      <h1>Items in your pantry:</h1>
      <table>
        <thead>
          <tr>
            <th>Item</th>
            <th>Quantity</th>
            <th>ID</th>
          </tr>
        </thead>
        <tbody>
          {pantry.map((p) => (
            <tr key={p.item_id}>
              <td>{p.name}</td>
              <td>{p.quantity}
                <button onClick={handleAdd.bind(this, p)}>+</button>
                <button onClick={handleSubtract.bind(this, p)}>-</button>
              </td>
              <td>{p.item_id}</td>
              <td>
                <button onClick={handleDelete.bind(this, p.id)}>Delete this item</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;