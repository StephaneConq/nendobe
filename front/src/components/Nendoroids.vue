<template>
    <div class="full-width">
        <v-row class="full-width">
            <v-col cols="12" sm="6">
                <v-chip-group v-model="tab" selected-class="text-primary" column>
                    <v-chip v-for="n in nendoroids" :key="n.id" @click="modelChanged(n)">
                        {{ n.name }}
                    </v-chip>
                </v-chip-group>
            </v-col>
        </v-row>
        <NendoroidItem v-if="selectedNendoroid" />
        <NendoroidPrices v-if="selectedNendoroid" />
    </div>
</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';
import NendoroidItem from '@/components/NendoroidItem.vue';
import NendoroidPrices from '@/components/NendoroidPrices.vue';

export default {
    data: () => ({
        tab: []
    }),
    components: {
        NendoroidItem,
        NendoroidPrices
    },
    setup() {
        const store = useStore();
        const nendoroids = computed(() => store.state.nendoroidsStore.currentNendoroids);
        const selectedNendoroid = computed(() =>  store.state.nendoroidsStore.selectedNendoroid);

        const modelChanged = (event) => {
            store.commit('nendoroidsStore/setSelectedNendoroid', null);
            setTimeout(() => {
                store.commit('nendoroidsStore/setSelectedNendoroid', event);
            }, 100);
        }
        
        return {
            nendoroids,
            modelChanged,
            selectedNendoroid
        }
    }
}

</script>

<style>

</style>