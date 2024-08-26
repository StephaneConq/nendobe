<template>

    <v-row class="container">
        <v-col cols="8">
            <v-text-field v-model="modelId" hide-details="auto" label="Saisir un id de Nendoroid"></v-text-field>
        </v-col>

        <v-col cols="4" class="button-container">
            <v-btn @click="searchById" icon="mdi-send" size="small"></v-btn>
            <v-btn @click="triggerInputfile" icon="mdi-camera" size="small"></v-btn>
            <input @change="fileUploaded" type="file" id="input-file" accept="image/*" capture="environment"/>
        </v-col>
    </v-row>

</template>

<script>
import { useStore } from 'vuex';
import { ref } from 'vue';

export default {
    setup() {

        const store = useStore();
        
        const fileUploaded = (event) => {
            store.dispatch('imageStore/sendFile', event.target.files[0]);
        }

        const triggerInputfile = () => {
            const input = document.getElementById('input-file');
            input.click();
        }

        const modelId = ref('');

        const searchById = () => {
            console.log('modelId', modelId.value);
            store.dispatch('nendoroidsStore/getNendoroidById', modelId.value);
        }

        return {
            triggerInputfile,
            fileUploaded,
            searchById,
            modelId
        }
    }
}

</script>

<style scoped>
.container {
    width: 100%;
    padding: 10px;
}

.button-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#input-file {
    display: none;
}
</style>