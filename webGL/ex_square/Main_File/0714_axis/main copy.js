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

		const scene = new THREE.Scene();
		this._scene = scene;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();
        // this._update_position();

		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));

        // raycaster 초기화
        this._raycaster = new THREE.Raycaster();
	}

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100000);
		camera.position.z = 10;
        camera.lookAt(new THREE.Vector3(0, -15, 0)); // 원하는 방향으로 설정
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
		const axesHelper = new THREE.AxesHelper(50);
 		scene.add(axesHelper);
		 const labelSize = 2;
		 const labelGeometry = new THREE.PlaneGeometry(labelSize, labelSize);
		 const labelMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.6 });
		 
		 const labelX = new THREE.Mesh(labelGeometry, labelMaterial);
		 labelX.position.set(50, 0, 0);
		 this._scene.add(labelX);
	   
		 const labelY = new THREE.Mesh(labelGeometry, labelMaterial);
		 labelY.position.set(0, 50, 0);
		 this._scene.add(labelY);
	   
		 const labelZ = new THREE.Mesh(labelGeometry, labelMaterial);
		 labelZ.position.set(0, 0, 50);
		 this._scene.add(labelZ);

		// 3d object 생성 및 scene에 추가
		const solarSystem = new THREE.Object3D()
		this._scene.add(solarSystem)

		// 3d object detail
		const radius = 1
		const widthSegments = 20
		const heightSegments = 10
		const sphereGeometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments)
		const sunMaterial = new THREE.MeshPhongMaterial({
			emissive: 0xff0000, flatShading: false, wireframe: true })
		
		const sunMesh =  new THREE.Mesh(sphereGeometry, sunMaterial)
		sunMesh.scale.set(3,3,3) // 3배의 크기로 표시되기 위해
		solarSystem.name = 'solarSystem'
		solarSystem.add(sunMesh)
		
		
		const earthOrbit = new THREE.Object3D()
		solarSystem.add(earthOrbit)

		const earthMaterial = new THREE.MeshPhongMaterial({
			color: 0x2233ff, emissive: 0x112244, flatShading: true })

		const earthMesh = new THREE.Mesh(sphereGeometry, earthMaterial)
		// 애초에 solarsystem에 추가되어 솔라시스템을 기점으로 회전할 것
		earthOrbit.position.x =  10
		earthOrbit.add(earthMesh)

		// console.log(solarSystem)
		
		const moonOrbit = new THREE.Object3D()
		// 상대경로 설정해야 함
		moonOrbit.position.x =  2
		earthOrbit.add(moonOrbit)

		const moonMaterial = new THREE.MeshPhongMaterial({
			color: 0x8888888, emissive: 0x222222, flatShading: true	})

		const moonMesh = new THREE.Mesh(sphereGeometry, moonMaterial)
		moonMesh.scale.set(0.5, 0.5, 0.5)
		moonOrbit.add(moonMesh)
		moonOrbit.name = 'moonOrbit'
		console.log(moonOrbit.position.x)



		// 다른 함수에서 참조할 수 있도록 this에 할당한다
		this._solarSystem = solarSystem
		this._earthOrbit = earthOrbit

	}

    // setcontorl 초기
	_setControls() {
		const controls = new OrbitControls(this._camera, this._divContainer);
		this._controls = controls;
	}


// 수정
    _setControls() {
        const controls = new OrbitControls(this._camera, this._divContainer);
        // this._divContainer.addEventListener('change', this._handleControlsChange.bind(this));
        // this._divContainer.addEventListener('click', this._handleSphereClick.bind(this));
        this._controls = controls;
        

    }
    // _handleControlsChange() {
    //     // 필요한 경우 처리할 로직 추가
    // }
    
    // _handleSphereClick(event) {
    //     event.preventDefault();
        
    //     this._raycaster.setFromCamera({ x: 0, y: 0 }, this._camera);
        
    //     // console.log(this._raycaster)
    //     const intersects = this._raycaster.intersectObject(this._particle);
    
    //     if (intersects.length > 0) {
    //         // 클릭한 별에게 접근 가능, 
    //         console.log('intersects:' , intersects[0].object.position);
    //         const targetUrl = 'h1/index.html'
    //         window.location.href = targetUrl;
    //     }
    // }
    
// 수정

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
		this._solarSystem.rotation.y = time / 100
		this._earthOrbit.rotation.y = time

		// this._earthOrbit.rotation.z = time
		// this._particle.rotation.y = time;
		// this._particle.rotation.z = time;
        // console.log(this._particle)
	}

    // _update_position() {
    //     console.log('x: ',this._particle.position.x,'   ','y:',this._particle.position.y)
        
    // }
}

window.onload = function () {
	new App();
};