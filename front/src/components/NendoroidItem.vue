<template>

    <v-row class="full-width">
        <v-col cols="6" class="img-container">
            <a :href="selectedNendoroid.link" target="_blank">
                <img :src="selectedNendoroid?.img" alt="image" class="image">
            </a>
        </v-col>

        <v-col cols="6" class="nendoroid-infos">
            <span>Nendoroid n°{{ selectedNendoroid?.id }}</span>
            <span>{{ selectedNendoroid?.name }}</span>
            <span>Prix min : {{ priceMin }} €</span>
            <span>Prix max : {{ priceMax }} €</span>
            <span>Prix moyen : {{ averagePrice }} €</span>
        </v-col>
    </v-row>

</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    setup() {
        const store = useStore();

        const selectedNendoroid = computed(() => store.state.nendoroidsStore.selectedNendoroid);
        const prices = computed(() =>  store.state.nendoroidsStore.prices);

        const getAllPrices = (localPrices) => {
            let allPrices = [];
            Object.keys(localPrices).forEach(key => {
                allPrices = [...allPrices, ...localPrices[key].map(p => p.price)];
            });
            return allPrices;
        };

        const allPrices = getAllPrices(prices.value[selectedNendoroid.value.id]);

        return {
            selectedNendoroid,
            prices,
            priceMin: Math.round(Math.min(...allPrices) * 100) / 100,
            priceMax: Math.round(Math.max(...allPrices) * 100) / 100,
            averagePrice: Math.round(allPrices.reduce((a, b) => a + b, 0) / allPrices.length * 100) / 100
        }
    }
}
</script>

<style>
.nendoroid-infos {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.img-container,
.nendoroid-infos {
    text-align: center;
    width: 100%;
}
</style>