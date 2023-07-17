import React, { useRef } from 'react';
// import { useFrame } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';
// import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { Canvas } from '@react-three/fiber';

const Star = () => {
  const particlesRef = useRef();

  const randomPointInSphere = (radius) => {
    const x = THREE.MathUtils.randFloat(-1, 1);
    const y = THREE.MathUtils.randFloat(-1, 1);
    const normalizationFactor = 1 / Math.sqrt(x * x + y * y);

    return new THREE.Vector3(
      x * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, 1.2 * radius),
      y * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, 1.2 * radius),
      0
    );
  };

  const initPoints = () => {
    const geometry = new THREE.BufferGeometry();
    const positions = [];

    const particlesCount = 15000;

    for (let i = 0; i < particlesCount; i++) {
      const vertex = randomPointInSphere(100);
      positions.push(vertex.x, vertex.y, 0);
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

    const particleTexture = new THREE.TextureLoader().load('/textures/particles/star.png');
    const particlesMaterial = new THREE.PointsMaterial({
      map: particleTexture,
      size: 0.5,
      sizeAttenuation: true,
    });

    const stars = new THREE.Points(geometry, particlesMaterial);
    particlesRef.current.add(stars);
  };

  React.useEffect(() => {
    initPoints();
  }, [initPoints]);
  
}

export default function Star() {
    return (
        <div style={{ width: '100%', height: '100vh', background: 'black' }}>
        <Canvas>
          <ambientLight intensity={2} position={[0, 0, 0]} />
          <pointLight intensity={2} position={[0, 0, 0]} />
          <Star />
          <OrbitControls />
        </Canvas>
      </div>
    );
}

