<template>

    <v-row class="container">
        <v-col cols="9">
            <v-text-field hide-details="auto" label="Saisir un id de Nendoroid"></v-text-field>
        </v-col>

        <v-col cols="3" class="button-container">
            <v-btn @click="triggerInputfile" icon="mdi-camera" size="large"></v-btn>
            <input @change="fileUploaded" type="file" id="input-file" accept="image/*" capture="environment"/>
        </v-col>
    </v-row>

</template>

<script>
import { useStore } from 'vuex';

export default {
    setup() {

        const store = useStore();
        
        const fileUploaded = (event) => {
            store.dispatch('imageStore/sendFile', event.target.files[0]);
        }

        const triggerInputfile = () => {
            const  input = document.getElementById('input-file');
            input.click();
        }

        return {
            triggerInputfile,
            fileUploaded
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
    justify-content: center;
    align-items: center;
}

#input-file {
    display: none;
}
</style>