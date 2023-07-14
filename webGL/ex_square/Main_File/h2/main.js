import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

let camera, renderer, scene, controls, particles;

function init() {
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);

  document.body.appendChild(renderer.domElement);

  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
  camera.position.set(100, 0, 100);
  
  controls = new OrbitControls(camera, renderer.domElement);

  // Create axes
  const axesHelper = new THREE.AxesHelper(50);
  scene.add(axesHelper);

  // Create number labels for axes
  const labelSize = 2;
  const labelGeometry = new THREE.PlaneGeometry(labelSize, labelSize);
  const labelMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.6 });
  
  const labelX = new THREE.Mesh(labelGeometry, labelMaterial);
  labelX.position.set(50, 0, 0);
  scene.add(labelX);

  const labelY = new THREE.Mesh(labelGeometry, labelMaterial);
  labelY.position.set(0, 50, 0);
  scene.add(labelY);

  const labelZ = new THREE.Mesh(labelGeometry, labelMaterial);
  labelZ.position.set(0, 0, 50);
  scene.add(labelZ);

  // Add number texts to labels
  const labelFont = "Arial";
  const labelFontSize = 20;

  const labelTextX = createTextLabel("X", labelFont, labelFontSize);
  labelTextX.position.set(labelSize / 2, labelSize / 2, 0.01);
  labelX.add(labelTextX);

  const labelTextY = createTextLabel("Y", labelFont, labelFontSize);
  labelTextY.position.set(labelSize / 2, labelSize / 2, 0.01);
  labelY.add(labelTextY);

  const labelTextZ = createTextLabel("Z", labelFont, labelFontSize);
  labelTextZ.position.set(labelSize / 2, labelSize / 2, 0.01);
  labelZ.add(labelTextZ);
}

function createTextLabel(text, font, size) {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  context.font = `${size}px ${font}`;

  const width = context.measureText(text).width;
  const height = size;

  canvas.width = width;
  canvas.height = height;

  context.font = `${size}px ${font}`;
  context.fillStyle = 'white';
  context.fillText(text, 0, size);

  const texture = new THREE.CanvasTexture(canvas);
  const material = new THREE.MeshBasicMaterial({ map: texture, transparent: true });

  const label = new THREE.Mesh(new THREE.PlaneGeometry(width, height), material);
  label.scale.set(0.1, 0.1, 0.1);

  return label;
}

const v = new THREE.Vector3();

function randomPointInSphere(radius) {
  const x = THREE.MathUtils.randFloat(-1, 1);
  const y = THREE.MathUtils.randFloat(-1, 1);
  const normalizationFactor = 1 / Math.sqrt(x * x + y * y);

  v.x = x * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, 1.2 * radius);
  v.y = y * normalizationFactor * THREE.MathUtils.randFloat(0.5 * radius, 1.2 * radius);
  v.z = 0;

  return v;
}

function initPoints() {
  const geometry = new THREE.BufferGeometry();
  const positions = [];

  for (let i = 0; i < 50000; i++) {
    const vertex = randomPointInSphere(50);
    positions.push(vertex.x, vertex.y, 0);
  }

  geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({ color: 0xff00ff, size: 0.1 });
  particles = new THREE.Points(geometry, material);
  scene.add(particles);
}

function animate() {
  requestAnimationFrame(animate);
  // Rotate the particles
  particles.rotation.z += 0.001;
  renderer.render(scene, camera);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener('resize', onWindowResize);

init();
initPoints();
animate();
