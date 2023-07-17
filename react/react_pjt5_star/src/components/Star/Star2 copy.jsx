import React, { useEffect, useRef } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';

const StarField = () => {
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

    for (let i = 0; i < 50000; i++) {
      const vertex = randomPointInSphere(50);
      positions.push(vertex.x, vertex.y, 0);
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({ color: 0xff00ff, size: 0.1 });
    const particles = new THREE.Points(geometry, material);
    particlesRef.current.add(particles);
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
