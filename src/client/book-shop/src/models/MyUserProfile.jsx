class MyUserProfile {
    constructor(response) {
        this.user_id = response.id ? response.id : null;
        this.email = response.sub ? response.sub : null;
        this.first_name = response.first_name ? response.first_name : null;
        this.last_name = response.last_name ? response.last_name : null;
        this.telephone = response.telephone ? response.telephone : null;
        this.address = response.address ? response.address : null;
        this.addition_detail = response.addition_detail ? response.addition_detail : null;
        this.date_of_birth = response.date_of_birth ? response.date_of_birth : null;
        this.photo_url = response.photo_url ? response.photo_url : null;
    }
}
export default MyUserProfile;
