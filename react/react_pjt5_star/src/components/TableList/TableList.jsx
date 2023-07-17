import React, { useState } from 'react';
import AddTable from './AddTable';
// import Table from './Table';


export default function TableList() {

    const [tables, setTables] = useState([
        {id: '123', list: 
        [[1,10,1],[2,10,3],[4,10,4],[6,10,-1],[10,10,7] ]},
    ])

    const handleAdd = (table) => setTables([...tables, table])

    const formatList = (list) => {
        return list.map((item) => `[${item.join(', ')}]`).join(', ');
    };

    return (
        <div>
            <ul>
                {/* {tables.map((item) => (
                <li
                    key={item.id}
                >{item.list}</li>))} */}
                {tables.map((item) => (
                    <li key={item.id}>{formatList(item.list)}</li>
                ))}
                
                
                {/* {tables.map((item) => (
                    <Table
                    key={item.id}
                    todo={item}
                    />
                ))} */}
            </ul>
            <AddTable onAdd={handleAdd}/>
        </div>
    );
}

