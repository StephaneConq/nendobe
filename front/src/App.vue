<template>
  <v-app>
    <v-progress-linear v-if="loading" indeterminate></v-progress-linear>
    <v-main>
      <div class="img-container">
        <img src="@/assets/goodsmile_logo.jpg" />
      </div>
      <router-view />
      <Snackbar />
    </v-main>
  </v-app>
</template>

<script>
import { computed, watch } from 'vue';
import { useStore } from 'vuex';
import Snackbar from '@/components/Snackbar.vue';

export default {
  name: 'App',
  components: {
    Snackbar
  },
  setup() {
    const store = useStore();

    const loading = computed(() => store.getters['utilsStore/globalLoading']);

    return {
      loading
    }
  }
}
</script>

<style scoped>
.img-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

.img-container img {
  width: 25%;
}
</style>
