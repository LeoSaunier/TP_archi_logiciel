<script>
import { ref } from 'vue';

export default {
    setup() {
        const visible = ref(false);
        const questionnaire = ref({
            name: ''
        });
        return {
            visible,
            questionnaire
        }
    },
    methods: {
        addQuestionnaire() {
            const request = {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.questionnaire)
            };
            fetch("http://127.0.0.1:5000/quizz/api/v1.0/questionnaires", request)
            .then(response => {
                if (response.ok) {
                    console.log("Questionnaire added successfully");
                    this.$emit('UpdateQuestionnaire', this.questionnaire);
                    this.questionnaire.title = '';
                    this.visible = false;
                } else if (response.status === 400) {
                    console.error("Bad request");
                } else if (response.status === 403) {
                    console.error("You do not have permission to add this questionnaire");
                } else if (response.status === 500) {
                    console.error("Server error while adding questionnaire");
                } else {
                    console.error("Failed to add questionnaire");
                }
            })
            .catch(error => {
                console.error("Error adding questionnaire:", error);
            });
        }
    },
    emits : ["UpdateQuestionnaire"]
}

</script>

<template>
    <div>
        <button @click="visible = !visible">{{ visible ? `Masquer l'ajout` : 'Ajouter un questionnaire' }}</button>
        <div v-if="visible">
            <label>
                <input type="text" v-model="questionnaire.name" placeholder="Nom du questionnaire">
            </label>
            <button class="btn btn-add" @click="addQuestionnaire">Ajouter</button>
        </div>
    </div>


</template>