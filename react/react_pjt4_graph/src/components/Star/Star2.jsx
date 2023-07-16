import React, { useEffect, useRef } from 'react';
// import { Canvas } from '@react-three/fiber';
// import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';


const StarField = () => {
  const particlesRef = useRef();

  const randomPointInSphere = (radius) => {
    const x = THREE.MathUtils.randFloat(-1, 1);
    const y = THREE.MathUtils.randFloat(-1, 1);
    const normalizationFactor = 1 / Math.sqrt(x * x + y * y);

    const mul_num = 1.2

    return new THREE.Vector3(
      x * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, mul_num * radius),
      y * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, mul_num * radius),
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

    const particleTexture = new THREE.TextureLoader().load('.components/particles/star.png');
    const particlesMaterial = new THREE.PointsMaterial({
      map: particleTexture,
      size: 0.5,
      sizeAttenuation: true,
    });

    const stars = new THREE.Points(geometry, particlesMaterial);
    particlesRef.current.add(stars);
  };

  useEffect(() => {
    initPoints();
  }, []);

  return (
    <group>
      <axesHelper args={[50]} />
      <group ref={particlesRef} />
    </group>
  );
};

export default StarField;
