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

  export const deletePantryItem = async id => {
    const response = await fetch(`${APIURL}/items/${id}`, {
      method: "DELETE",
      mode: "cors",
      cache: "no-cache"
    });
    return;
  };

  export const editPantryItem = async data => {
    const response = await fetch(`${APIURL}/items/${data.id}`, {
      method: "PUT",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });
    return;
  };