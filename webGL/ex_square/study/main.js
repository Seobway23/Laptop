import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

class App {
	constructor() {
		const divContainer = document.querySelector("#webgl-container");
		this._divContainer = divContainer;

		const renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setPixelRatio(window.devicePixelRatio);
		divContainer.appendChild(renderer.domElement);
		this._renderer = renderer;

		const scene = new THREE.Scene();66
		this._scene = scene;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();


		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));
	}

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100);
		camera.position.z = 2;
		this._camera = camera;

	}

	_setupLight() {
		const color = 0xffffff;
		const intensity = 1;
		const light = new THREE.DirectionalLight(color, intensity);
		light.position.set(-1, 2, 4);
		this._scene.add(light);
	}

	_setupModel() {
		const geometry = new THREE.BoxGeometry(1, 1, 1);
		const fillmaterial = new THREE.MeshPhongMaterial({ color: 0x44a88  });
		const cube = new THREE.Mesh(geometry, fillmaterial);
		// const cube = new THREE.Mesh(geometry, material);
		
		const lineMaterial = new THREE.LineBasicMaterial({color: 0x44a88 });
		const line = new THREE.LineSegments(
			new THREE.WireframeGeometry(geometry), lineMaterial,
		)

		this._scene.add(cube);
		this._cube = cube;
	}

	_setControls() {
		new OrbitControls(this._camera, this._divContainer);
	}


	// _setupModel() {
	// 	const geometry = new THREE.SphereGeometry( 15, 32, 16 ); 
	// 	const material = new THREE.MeshBasicMaterial( { color: 0xffff00 } ); 
	// 	const sphere = new THREE.Mesh( geometry, material ); 
	// 	scene.add( sphere );

	// 	this._scene.add(THREE.Sphere);
	// 	this._sphere = sphere;
	// }

	resize() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;

		this._camera.aspect = width / height;
		this._camera.updateProjectionMatrix();

		this._renderer.setSize(width, height);
	}

	render(time) {
		this._renderer.render(this._scene, this._camera);
		this.update(time);
		requestAnimationFrame(this.render.bind(this));
	}

	update(time) {
		time *= 0.001; // secondunit
		// this._cube.rotation.x = time;
		// this._cube.rotation.y = time;
		// this._cube.rotation.z = time;

	}
}

window.onload = function () {
	new App();
};