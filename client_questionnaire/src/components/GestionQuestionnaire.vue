<script>

export default {
    props : {
        questionnaire: Object
    },
    methods: {
        addQuestionnaire() {
            console.log("addQuestionnaire");
        }
    },
    emits : ["addQuestionnaire"]
}

const selected = ref(false);
</script>

<template>
    <div>
        <div v-if="selected">
            <div v-for="question in questionnaire.questions"
                :question="question"
                @deleteQuestion="deleteQuestion">
            
            </div>
            <label>
                <input type="text" v-model="questionnaire.title" placeholder="Nom du questionnaire">
                <input type="text" v-model="questionnaire.description" placeholder="Description du questionnaire">
            </label>
            <button class="btn btn-add" @click="addQuestionnaire">Ajouter</button>
        </div>
    </div>


</template>