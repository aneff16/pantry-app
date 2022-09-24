const APIURL = 'http://localhost:5000'

export const getPantry = async () => {
    const res = await fetch(`${APIURL}/items`);
    return res.json();
  };

  export const addPantryItem = async item => {
    const response = await fetch(`${APIURL}/items`, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(item)
    });
    return;
  };

  export const deletePantryItem = async item => {
    const response = await fetch(`${APIURL}/items/${item.item_id}`, {
      method: "DELETE",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(item)
    });
    return;
  };

  export const editPantryItem = async item => {
    const response = await fetch(`${APIURL}/items/${item.item_id}`, {
      method: "PUT",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(item)
    });
    return;
  };