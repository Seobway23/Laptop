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
		const points = [];
		this._points = points;

		this._setupCamera();
		this._setupLight();
		this._setupModel();
		this._setControls();
        // this._update_position();

		// console.log( 'controls:', this._controls.target)
		// this._controls.target.set(0, 100, 0);
		// console.log( 'controls:', this._controls.target)

		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));

        // raycaster 초기화
        this._raycaster = new THREE.Raycaster();
        this._mouse = new THREE.Vector2();

		 // Add click event listener
		 this._divContainer.addEventListener('click', this._handleClick.bind(this));

	}

	_handleClick(event) {
        event.preventDefault();

        // Calculate normalized device coordinates (NDC) from mouse coordinates
        const containerWidth = this._divContainer.clientWidth;
        const containerHeight = this._divContainer.clientHeight;
        const x = (event.clientX / containerWidth) * 2 - 1;
        const y = -(event.clientY / containerHeight) * 2 + 1;
        this._mouse.set(x, y);

		// console.log(x, y)

        // Raycasting
        this._raycaster.setFromCamera(this._mouse, this._camera);
        const intersects = this._raycaster.intersectObjects(this._scene.children, true);

		// console.log(intersects)
		// console.log(this._points)

        // Apply lighting effect to clicked object
        if (intersects.length > 0) {
			// console.log(intersects)
			console.log(11111111111)
            const clickedObject = intersects[0].object;
			// console.log(clickedObject)

			const clickPoint = clickedObject.uuid

			const objectWithUUIDA = this._points.find(object => object.uuid === clickPoint)
			console.log(objectWithUUIDA.url)
			console.log(objectWithUUIDA.position)

		
		
		}
    }

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 90);
		camera.position.set(0, -10, 0)
		// camera.position.x = 40
		// camera.position.z = 10
        camera.lookAt(new THREE.Vector3(0,0,1)); // 원하는 방향으로 설정
		this._camera = camera

	}

	_setupLight() {
		const color = 0xffffff;
		const intensity = 1;
		const light = new THREE.DirectionalLight(color, intensity);
		light.position.set(-1, 2, 4);
		this._scene.add(light);
	}

	_setupModel() {
		// axis
		const axesHelper = new THREE.AxesHelper(10);
 		this._scene.add(axesHelper);

		const smul = 5
		const starx = [0,1,3,4,6,7,8]
		const stary = [1,1,1,1,1,1,1]
		const starz = [1,0,0,1,3,4,5]
		
		const starSystem = new THREE.Object3D()
		this._scene.add(starSystem)
											//radius, widthSegments, heightSegments
		const sphereGeometry = new THREE.SphereGeometry(0.1, 30, 30)
		const sphereMeterial = new THREE.MeshPhongMaterial({
			color: 0x2233ff,
			emissive: 0xffff00, flatShading: false, wireframe: false })
		
			

		
		for (let one = 0; one < starx.length; one ++) {
			const starMesh = new THREE.Mesh(sphereGeometry, sphereMeterial)
			starSystem.name = 'starSystem'
			starMesh.position.x = starx[one]
			console.log('X: ',starx[one], ' Y: ',stary[one],' Z:',starz[one])
			starMesh.position.y = stary[one] * smul
			starMesh.position.z = starz[one]
			starSystem.add(starMesh)

			// console.log(starSystem[0].position)

			this._starSystem = starSystem
		}
		// console.log(starSystem)

	}

    // setcontorl 초기
	_setControls() {
		const controls = new OrbitControls(this._camera, this._divContainer);
		// const containerHeight = this._divContainer.clientHeight;
		// const targetY = -(containerHeight * 0.25); // Adjust the value (0.25) as needed
		// controls.target.set(0, 100, 0);
		// const defaultRotationAxis = new THREE.Vector3(0, 10000000000, 0);
		// controls.target.copy(defaultRotationAxis);
		// controls.autoRotateSpeed = 3
		// controls.enableDamping = true;
		// controls.dampingFactor = 0.05;
		// controls.enableZoom = true;
		// controls.minDistance = 100;
		// controls.maxDistance = 300;
		// controls.enablePan = true;

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
		// this._solarSystem.rotation.y = time / 5
		// this._earthOrbit.rotation.y = time
		this._starSystem.rotation.z = time / 5 

		for ( let g = 0; g < this._points.length; g ++) {
			this._points[g].rotation.x = time / 5
			this._points[g].rotation.y = time / 5

		}

		// // galaxy2 rotate
		// this._points[0].rotation.x = time / 5
		// this._points[0].rotation.y = time / 5

		// //galaxy3 rotate
		// this._points[1].rotation.x = time /5
		// this._points[1].rotation.z = time /5
		

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

export default App;

