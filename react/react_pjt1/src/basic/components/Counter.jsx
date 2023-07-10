import React, { useState } from 'react';

export default function AppCounter() {
    const [count, setCount] = useState(0);
    return (
        <div className="counter">
            <span className='number'> {count} </span>
            <button className="button"
                onClick={()=> {
                    setCount((prev)=> prev+1);
                    setCount((prev)=> prev+1);
                    setCount((prev)=> prev+1);
                    setCount((prev)=> prev+1);
                    setCount((prev)=> prev+1);
                    // 이전 값들을 전달받아서 업데이트할 수 있도록
                    // 콜백함수로 해야 안전하다

                }}
            
            > Add +</button>
        </div>
    );
}

