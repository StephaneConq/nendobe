
export const generateName = (nendoroid) => {
    let lowerName = nendoroid.name.toLowerCase();
    if (lowerName.includes('nendoroid')) {
        lowerName = lowerName.replace('nendoroid', `nendoroid ${nendoroid.id} - `);
    } else {
        lowerName = `nendoroid ${nendoroid.id} - ${nendoroid.name}`;
    }
    return lowerName;
}