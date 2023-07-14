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

		window.onresize = this.resize.bind(this);
		this.resize();

		requestAnimationFrame(this.render.bind(this));

        // raycaster 초기화
        this._raycaster = new THREE.Raycaster();
	}

	// 375, 667

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 90);
		camera.position.x = 40
		camera.position.z = 10
        camera.lookAt(new THREE.Vector3(0,0,0)); // 원하는 방향으로 설정
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
		
		
		// earth
		const earthOrbit = new THREE.Object3D()
		solarSystem.add(earthOrbit)
	
		const earthMaterial = new THREE.MeshPhongMaterial({
			color: 0x2233ff, emissive: 0x112244, flatShading: true })

		const earthMesh = new THREE.Mesh(sphereGeometry, earthMaterial)
		earthOrbit.position.x =  10
		earthOrbit.add(earthMesh)
		
		// moon
		const moonOrbit = new THREE.Object3D()
		moonOrbit.position.x =  2
		earthOrbit.add(moonOrbit)

		const moonMaterial = new THREE.MeshPhongMaterial({
			color: 0x8888888, emissive: 0x222222, flatShading: true	})

		const moonMesh = new THREE.Mesh(sphereGeometry, moonMaterial)
		moonMesh.scale.set(0.5, 0.5, 0.5)
		moonOrbit.add(moonMesh)
		moonOrbit.name = 'moonOrbit'
		console.log(moonOrbit.position.x)
		
		//bloom 해야할 듯

		// galaxy1
		const galaxyOrbit1 = new THREE.Object3D()
		solarSystem.add(galaxyOrbit1)
		
		const color = new THREE.Color(Math.random() * 0xffffff);

		const galaxyMaterial = new THREE.MeshPhongMaterial({
			color: color, emissive: 0x112244, flatShading: true })

		const galaxyMesh = new THREE.Mesh(sphereGeometry, galaxyMaterial)
		// 애초에 solarsystem에 추가되어 솔라시스템을 기점으로 회전할 것
		galaxyOrbit1.position.x =  10
		galaxyOrbit1.position.y = 10
		galaxyOrbit1.position.z = 10
		galaxyOrbit1.add(galaxyMesh)

		// galaxyOrbit2
		const galaxyOrbit2 = new THREE.Object3D()
		solarSystem.add(galaxyOrbit2)

		const color2 = new THREE.Color(Math.random() * 0xffffff);

		const galaxy2Material = new THREE.MeshPhongMaterial({
			color: color2, emissive: 0x112244, flatShading: true })

		const galaxy2Mesh = new THREE.Mesh(sphereGeometry, galaxy2Material)
		// 애초에 solarsystem에 추가되어 솔라시스템을 기점으로 회전할 것
		galaxyOrbit2.position.x = -10
		galaxyOrbit2.position.y = 10
		galaxyOrbit2.position.z = 10
		galaxyOrbit2.add(galaxy2Mesh)

		// 방향 설정
		const dx = [-10 / Math.sqrt(2),-10,-10  / Math.sqrt(2), 0, 0, 10  / Math.sqrt(2), 10, 10  / Math.sqrt(2)]
		const dy = [15 , 15, 15, 15, 15, 15, 15, 15]
		const dz = [10  / Math.sqrt(2), 0, -10 / Math.sqrt(2), 10, -10, 10  / Math.sqrt(2), 0, -10  / Math.sqrt(2)]
		// galaxy2
		for ( let ig = 0 ; ig < 8; ig ++) {
			console.log(ig)
			const vertices = []

			const color_ig = new THREE.Color(Math.random() * 0xffffff);
			for (let i = 0; i<1000; i++) {
				const x = THREE.MathUtils.randFloatSpread(5);
				const y = THREE.MathUtils.randFloatSpread(5);
				const z = THREE.MathUtils.randFloatSpread(5);
				vertices.push(x ,y ,z)
			}
			const geometry = new THREE.BufferGeometry()
			geometry.setAttribute(
				'position',	new THREE.Float32BufferAttribute(vertices, 3));
			const material = new THREE.PointsMaterial({
				color: color_ig, size: 2, sizeAttenuation: false })
			const point = new THREE.Points(geometry, material)
			point.position.x = dx[ig]*1.2
			point.position.y = dy[ig]*1.2
			point.position.z = dz[ig]*1.2

			this._scene.add(point)
			solarSystem.add(point)
			this._points.push(point)
		}


		// const vertices = []
		// for (let i = 0; i<1000; i++) {
		// 	const x = THREE.MathUtils.randFloatSpread(10);
		// 	const y = THREE.MathUtils.randFloatSpread(10);
		// 	const z = THREE.MathUtils.randFloatSpread(10);
		// 	vertices.push(x ,y ,z)
		// }
		// const geometry = new THREE.BufferGeometry()
		// geometry.setAttribute(
		// 	'position',	new THREE.Float32BufferAttribute(vertices, 3));
		// const material = new THREE.PointsMaterial({
		// 	color: color, size: 2, sizeAttenuation: false })
		// const point = new THREE.Points(geometry, material)
		// point.position.x = 10
		// point.position.y = + 15
		// point.position.z = -10

		// this._scene.add(point)
		// solarSystem.add(point)
		// this._points.push(point)

		// galaxy3
		const vertices2 = []
		for (let i = 0; i<2000; i++) {
			const x = THREE.MathUtils.randFloatSpread(10);
			const y = THREE.MathUtils.randFloatSpread(10);
			const z = THREE.MathUtils.randFloatSpread(10);
			if (x**2 + y**2 + z**2 < 5**2 ){ 
				vertices2.push(x ,y ,z)
			}
		}

		// const color3 = new THREE.Color(Math.random() * 0xffffff);

		// const geometry2 = new THREE.BufferGeometry()
		// geometry2.setAttribute(
		// 	'position',	new THREE.Float32BufferAttribute(vertices2, 3));
		// const material2 = new THREE.PointsMaterial({
		// 	color: color3, size: 2, sizeAttenuation: false })
		// const point2 = new THREE.Points(geometry2, material2)
		// point2.position.x = -10
		// point2.position.y = +15
		// point2.position.z = -10

		// this._scene.add(point2)
		// solarSystem.add(point2)
		// this._points.push(point2)


		// 다른 함수에서 참조할 수 있도록 this에 할당한다
		this._solarSystem = solarSystem
		this._galaxyOrbit1 = galaxyOrbit1
		this._earthOrbit = earthOrbit

	}

    // setcontorl 초기
	_setControls() {
		const controls = new OrbitControls(this._camera, this._divContainer);

		const containerHeight = this._divContainer.clientHeight;
		const targetY = -(containerHeight * 0.25); // Adjust the value (0.25) as needed

		controls.target.set(0, targetY, 0);


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
		this._solarSystem.rotation.y = time / 5
		this._earthOrbit.rotation.y = time
		this._galaxyOrbit1.rotation.y = time

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