<script>

export default {
    methods: {
        addQuestionnaire() {
            console.log("addQuestionnaire");
        }
    },
    emits : ["addQuestionnaire"]
}

const visible = ref(false);
</script>

<template>
    <div>
        <button @click="visible = !visible">{{ visible ? `Masquer l'ajout` : 'Ajouter un questionnaire' }}</button>
        <div v-if="visible">
            <label>
                <input type="text" v-model="questionnaire.title" placeholder="Nom du questionnaire">
                <input type="text" v-model="questionnaire.description" placeholder="Description du questionnaire">
            </label>
            <button class="btn btn-add" @click="addQuestionnaire">Ajouter</button>
        </div>
    </div>


</template>