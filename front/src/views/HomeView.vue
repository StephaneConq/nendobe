<template>
  <Searchbar />
  <Nendoroids />
</template>

<script>
import { defineComponent } from 'vue';
import Searchbar from '@/components/Searchbar.vue';
import Nendoroids from '@/components/Nendoroids.vue';
// Components

export default defineComponent({
  name: 'HomeView',

  components: {
    Searchbar,
    Nendoroids
  },
});
</script>
