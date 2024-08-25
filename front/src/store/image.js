export default {
    namespaced: true,
    state: () => {

    },
    actions: {
        sendFile( {commit, dispatch}, file) {

            commit('utilsStore/setGlobalLoading', true, {root: true});
            commit('nendoroidsStore/setCurrentNendoroids', [], {root: true});
            commit('nendoroidsStore/setPrices', null, {root: true});
            commit('nendoroidsStore/setSelectedNendoroid', null, {root: true});

            const formData = new FormData();
            formData.append('image', file);

            fetch(`${import.meta.env.VITE_API_URL}/photo/process?content_type=${file.type}`, {
                method: 'POST',
                body: formData,
            }).then(res => {

                res.json().then((nendoroids) => {

                    commit('nendoroidsStore/setCurrentNendoroids', nendoroids, {root: true});
                    const promises = [];

                    nendoroids.forEach(nendoroid => {
                        promises.push(dispatch('nendoroidsStore/updatePrices', nendoroid.id, {root: true}));
                    });

                    Promise.all(promises).then(() => {
                        commit('utilsStore/setGlobalLoading', false, {root: true});
                    });
                   
                });                
            });
        }
    }
}