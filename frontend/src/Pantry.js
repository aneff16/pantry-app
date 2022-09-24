import { useEffect, useState } from "react";

function Pantry() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await fetch('http://localhost:5000');
            const responseItems = await response.json();
            setItems(responseItems);
        };

        fetchItems();
    }, []);

    return(
        <div>
            <h1>Items in your pantry:</h1>
            <div>
                {items.map((item) => (
                    <div key={item.id}>
                        <div>{item.name}</div>
                        <div>{item.quantity}</div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Pantry;