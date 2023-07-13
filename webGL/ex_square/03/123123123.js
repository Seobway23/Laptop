import * as THREE from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
// 렌더 루프 다시 해야 함
// 


class App {
	constructor() {
		// 전역 변수 설정

		// class 입히기 
		const divContainer = document.querySelector("#webgl-container");
		this._divContainer = divContainer;

		const particles = [];
		this._particles = particles


		const mouseX = 0, mouseY = 0;
		this._mouseX = mouseX, this._mouseY = mouseY;


		// 뭔지 잘 모름
		const renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setPixelRatio(window.devicePixelRatio);
		divContainer.appendChild(renderer.domElement);
		this._renderer = renderer;

		// 장면 추가 
		const scene = new THREE.Scene();
		this._scene = scene;

		this._setupCamera();
		this._setupLight();
		// this._setupModel();
		this._setControls();
		this._updateparticles();


		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));
	}

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100); // 시야 종횡비
		camera.position.z = 2; // 카메라 위치
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

		// particle 업데이트하기
		updateparticles();


	}

	_updateparticles() {
		var particle, material; 
		// we're gonna move from z position -1000 (far away) 
		// to 1000 (where the camera is) and add a random particle at every pos. 
		for ( var zpos= -1000; zpos < 1000; zpos+=20 ) {
			// we make a particle material and pass through the 
			// colour and custom particle render function we defined. 
			material = new THREE.PointsMaterial( { color: 0xffffff, size: 10} );
			// make the particle
			particle = new THREE.Points(new THREE.BufferGeometry(), material);
		
			// give it a random x and y position between -500 and 500
			particle.position.x = Math.random() * 1000 - 500;
			particle.position.y = Math.random() * 1000 - 500;
		
			// set its z position
			particle.position.z = zpos;
		
			// scale it up a bit
			particle.scale.x = particle.scale.y = 10;
		
			// add it to the scene
			this._scene.add( particle );
		
			// and to the array of particles. 
			this._particles.push(particle); 
		}

		for(var i=0; i<this._particles.length; i++) {
 
			particle = this._particles[i]; 
	 
			// and move it forward dependent on the mouseY position. 
			particle.position.z +=  this._mouseY * 0.1;
	 
			// if the particle is too close move it to the back
			if(particle.position.z>1000) particle.position.z-=2000; 
	 
		}

	}

	particleRender( context ) {
 
		// we get passed a reference to the canvas context
		context.beginPath();
		// and we just have to draw our shape at 0,0 - in this
		// case an arc from 0 to 2Pi radians or 360º - a full circle!
		context.arc( 0, 0, 1, 0,  Math.PI * 2, true );
		context.fill();
	}



}

window.onload = function () {
	new App();
};