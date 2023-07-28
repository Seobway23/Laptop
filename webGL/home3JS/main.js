import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

let scene, camera, renderer, stars, starMaterial, starGeo;

function init() {
  //create scene object
  scene = new THREE.Scene();

  //setup camera with facing upward
  camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    1,
    1000
  );
  camera.position.z = 1;
  camera.rotation.x = Math.PI / 2;

  //setup renderer
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  createStars();

  animate();
}

function createStars() {
  starGeo = new THREE.BufferGeometry();
  let vertices = [];
  let velocity = [];
  let acceleration = [];

  for (let i = 0; i < 6000; i++) {
    vertices.push(
      Math.random() * 600 - 300,
      Math.random() * 600 - 300,
      Math.random() * 600 - 300
    );
    velocity.push(0);
    acceleration.push(0.02);
  }

  starGeo.setAttribute(
    "position",
    new THREE.Float32BufferAttribute(vertices, 3)
  );
  starGeo.setAttribute(
    "velocity",
    new THREE.Float32BufferAttribute(velocity, 1)
  );
  starGeo.setAttribute(
    "acceleration",
    new THREE.Float32BufferAttribute(acceleration, 1)
  );

  let sprite = new THREE.TextureLoader().load("star.png");
  starMaterial = new THREE.PointsMaterial({
    color: 0xaaaaaa,
    size: 1,
    map: sprite,
  });

  stars = new THREE.Points(starGeo, starMaterial);
  scene.add(stars);
  let sphereGeometry = new THREE.SphereGeometry(50, 32, 32);
  let sphereMaterial = new THREE.MeshBasicMaterial({ color: 0x7777ff });
  let sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
  scene.add(sphere);
}

//rendering loop
function animate() {
  let position = stars.geometry.attributes.position;
  let velocity = stars.geometry.attributes.velocity;
  let acceleration = stars.geometry.attributes.acceleration;

  for (let i = 0; i < position.count; i++) {
    velocity.array[i] += acceleration.array[i];
    position.array[i * 3 + 1] -= velocity.array[i];

    if (position.array[i * 3 + 1] < -200) {
      position.array[i * 3 + 1] = 200;
      velocity.array[i] = 0;
    }
  }

  position.needsUpdate = true;

  stars.rotation.y += 0.002;

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}

init();
