<template>

    <v-card class="card">
        <v-tabs v-model="tab" bg-color="primary">
            <v-tab v-for="key in keys" :value="key">{{ key }}</v-tab>
        </v-tabs>

        <v-card-text class="list-container">
            <v-tabs-window v-model="tab">
                <v-tabs-window-item v-for="key in keys" :value="key">
                    <span v-if="!nendoroidPrices[key].length">Pas d'article trouvé dans ce store</span>

                    <v-row v-for="sale in getSortedPrices(nendoroidPrices[key])" :key="sale.url" class="list-item">
                        <v-col cols="4">
                            <img :src="sale.image" />
                        </v-col>
                        <v-col cols="8">
                            <a :href="sale.url" target="_blank">{{ sale.name }}</a><br />
                            <span>{{ Math.round(sale.price * 100) / 100 }} €</span>
                        </v-col>
                    </v-row>

                </v-tabs-window-item>
            </v-tabs-window>
        </v-card-text>
    </v-card>


</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    data: () => ({
        tab: null,
    }),
    setup() {
        const store = useStore();

        const nendoroid = computed(() => store.state.nendoroidsStore.selectedNendoroid);
        const allPrices = computed(() => store.state.nendoroidsStore.prices);

        const nendoroidPrices = allPrices.value[nendoroid.value.id];

        const getSortedPrices = (prices) => {
            return prices.sort((a, b) => a['price'] - b['price']);
        }

        return {
            nendoroidPrices,
            keys: Object.keys(nendoroidPrices),
            getSortedPrices
        }
    }
}

</script>

<style>
.list-item img {
    width: 100%;
}

.list-container {
    max-height: 300px;
    overflow-y: scroll;
}

.card {
    margin: 10px;
}
</style>