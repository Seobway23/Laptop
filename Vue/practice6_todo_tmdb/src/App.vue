<template>
  <div>
    <nav style="background-color: #e3f2fd">
      <ul class="nav justify-content-end" >
        <li>
          </li>
        <li class="nav-item">
          <router-link class="nav-link active" to="/movies">movies</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/random">radnom</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/watch-list">watch-list</router-link>
        </li>
      </ul>
    </nav>
    <router-view id="app"/>


  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#black1 {
  color: black;
}
</style>
