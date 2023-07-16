import './App.css';
import TableList from './components/TableList/TableList';
import Star from './components/Star/Star2';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';



function App() {
  return (
    <div>
      <h1>hello, this is the moon light</h1>
      <TableList/>
      <Canvas>
        <Star/>
        <OrbitControls />
      </Canvas>


    </div>
  );
}

export default App;
