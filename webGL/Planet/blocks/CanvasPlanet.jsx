import { Stats, OrbitControls, Sky, Environment } from "@react-three/drei";
import { Canvas, useLoader } from "@react-three/fiber";
import React from "react";
import * as THREE from "three";
import { FrontSide, Vector3 } from "three";
import { Ocean } from "react-three-ocean";
import night from "./bg-night.jpg";

const App = () => {
  // const [camera, setCamera] = useState();

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas
        camera={{
          position: [0, 200, 0],
          fov: 50,
          aspect: window.innerWidth / window.innerHeight,
          near: 0.1,
          far: 2000,
        }}
        dpr={window.devicePixelRatio}
        shadows
      >
        {/* canvas color */}
        <color attach="background" args={["#ffffff"]} />
        {/* fps */}
        <Stats />
        <Sky
          distance={3000}
          sunPosition={[1, 1, 0]}
          inclination={0.5}
          azimuth={0.1}
          mieCoefficient={0.003}
          rayleigh={0.1}
        />
        {/* camera controller */}
        <OrbitControls
          attach="orbitControls"
          enabled={true}
          rotateSpeed={-0.5}
          enablePan={false}
          minDistance={0}
          maxDistance={1000}
          autoRotate={true}
          autoRotateSpeed={0.5}
          // maxPolarAngle={Math.PI / 2}
        />
        {/* lights */}
        <ambientLight intensity={0.1} />
        <directionalLight
          intensity={1}
          position={[5, 5, 5]}
          castShadow
          shadow-mapSize-width={1024}
          shadow-mapSize-height={1024}
          shadow-bias={-0.003}
        />
        {/* objects */}
        <Ocean
          dimensions={[10000, 10000]}
          normals="https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/waternormals.jpg"
          distortionScale={20}
          size={3}
          options={{
            // defaults
            clipBias: 0,
            alpha: 2,
            waterNormals: null, // automatically set to provided texture from "normals" prop
            sunDirection: new Vector3(0.70707, 0.70707, 0),
            sunColor: 0xffffff,
            waterColor: 0x001e0f,
            eye: new Vector3(0, 0, 0),
            distortionScale: 3.7, // automatically set from "distortionScale" prop
            side: FrontSide,
            fog: false,
          }}
        />
        <>
          <Environment background blur={0} preset="park" />
          <mesh position={[50, 5, 0]}>
            <sphereGeometry args={[5, 32, 32]} />
            <meshStandardMaterial metalness={1} roughness={0} />
          </mesh>
        </>
        <mesh position={[50, 5, 50]}>
          <sphereGeometry args={[5, 32, 32]} />
          <meshNormalMaterial
          // envMap={texture}
          // metalness={1}
          // roughness={0}
          // color="blue"
          />
        </mesh>
        <mesh position={[0, 10, 50]}>
          <sphereGeometry args={[5, 32, 32]} />
          <meshStandardMaterial
            // color="blue"
            map={useLoader(THREE.TextureLoader, night)}
            // metalness={0.8}
            roughness={0.5}
            flatShading={false}
          />
        </mesh>
      </Canvas>
    </div>
  );
};

export default App;
