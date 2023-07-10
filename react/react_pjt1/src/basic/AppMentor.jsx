import React, { useState } from 'react';
import './App.css';

export default function Pointer() {
    const [person, setPerson] = useState({
        name: '엘리',
        title: '개발자',
        mentor: {
            name: '밥',
            title: '시니어개발자',
        },
    })
    return (
        <div>
            <h1>
                {person.name}는 {person.title}
            </h1>
            <p>
                {person.name}의 멘토는 {person.mentor.name} ({person.mentor.title})
            <button
            onClick={()=> {
                const name = prompt(`What's your mentor's name?`);
                const A = {...person}
                console.log('obj:',A)
                setPerson((person)=> ({...person, mentor: {...person.mentor, name:name}}));
            }}
            >
                멘토이름 바꾸기
            </button>

            <button
            onClick={() => {
                const title = prompt(`What's your mentor's title?`);
                setPerson((perv=> ({...person, mentor: {...person.mentor, title:title}})))
                console.log(person.mentor)
            }}>
                멘토 타이틀 바꾸기
            </button>

            </p>
        </div>
    );
}

