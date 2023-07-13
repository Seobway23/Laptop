import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

let camera, scene, renderer,
	mouseX = 0, mouseY = 0,
	particles = [];

init();

function init() {
	camera = new THREE.PerspectiveCamera(80, window.innerWidth / window.innerHeight, 1, 4000);
	camera.position.z = 1000;

	scene = new THREE.Scene();
	scene.add(camera);

	renderer = new THREE.WebGLRenderer();
	renderer.setSize(window.innerWidth, window.innerHeight);
	document.body.appendChild(renderer.domElement);

	makeParticles();
	setControls();

	document.addEventListener('mousemove', onMouseMove, false);

	update();
}

function update() {
	updateParticles();
	renderer.render(scene, camera);
	requestAnimationFrame(update);
}

function setControls() {
	const controls = new OrbitControls(camera, renderer.domElement);
	controls.enablePan = true; // Enable panning
	controls.enableZoom = true; // Enable zooming
	controls.enableRotate = true; // Enable orbiting
}

function makeParticles() {
	let particle, material;

	for (let zpos = -1000; zpos < 1000; zpos += 10) {
		const color = new THREE.Color(Math.random() * 0xffffff);

		material = new THREE.MeshBasicMaterial({ color: color });

		const geometry = new THREE.SphereGeometry(5, 16, 16);

		particle = new THREE.Mesh(geometry, material);

		particle.position.x = Math.random() * 1000 - 500;
		particle.position.y = Math.random() * 1000 - 500;
		particle.position.z = zpos;

		scene.add(particle);
		particles.push(particle);
	}
}

function updateParticles() {
	for (let i = 0; i < particles.length; i++) {
		const particle = particles[i];
		particle.position.z += mouseY * 0.1;

		if (particle.position.z > 1000) particle.position.z -= 2000;
	}
}

function onMouseMove(event) {
	mouseX = event.clientX - window.innerWidth / 2;
	mouseY = event.clientY - window.innerHeight / 2;
}
