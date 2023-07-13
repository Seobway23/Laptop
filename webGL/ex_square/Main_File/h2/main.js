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

	_setupCamera() {
		const width = this._divContainer.clientWidth;
		const height = this._divContainer.clientHeight;
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 100000);
		camera.position.z = 3;
        camera.lookAt(new THREE.Vector3(0, 0, 0)); // 원하는 방향으로 설정
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


		for ( let k = 0; k < 8; k++) {
			const vertices = []
			const t = 1000
			const dx = [t,0,0,t], dy = [0, 0, t, t]
			for (let i = 0; i<1000; i++) {
				const x = THREE.MathUtils.randFloatSpread(100);
				const y = THREE.MathUtils.randFloatSpread(100);
				const z = THREE.MathUtils.randFloatSpread(100);
				vertices.push(x + dx[k%4] ,y+ dy[k%4] ,z)
			}

			const geometry = new THREE.BufferGeometry()
			geometry.setAttribute(
				'position',
				new THREE.Float32BufferAttribute(vertices, 3)
			);
			
			// 색깔 조정 
			const color = new THREE.Color(Math.random() * 0xffffff);
			const material = new THREE.PointsMaterial({
				color: color,
				size: 3,
				sizeAttenuation: false
			})

			const point = new THREE.Points(geometry, material)
			this._scene.add(point)
			this._points.push(point)
			}
		
		
		console.log(this._points)
		for(let p=0; p< this.points; p++) {
			console.log(p)
			}
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
		time *= 0.00001; // secondunit
		let mul = 1
		this._points.forEach((element) =>{
			element.rotation.x =time * mul
			element.rotation.y =time * mul
			element.rotation.z =time * mul
			mul = mul +1;
			
		})
		// this._cube.rotation.x = time;
		// this._points.rotation.y = time;
		// this._points.rotation.z = time;
        // console.log(this._particle)
	}

    // _update_position() {
    //     console.log('x: ',this._particle.position.x,'   ','y:',this._particle.position.y)
        
    // }
}

window.onload = function () {
	new App();
};