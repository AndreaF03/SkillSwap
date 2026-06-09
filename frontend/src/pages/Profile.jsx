import { useState } from "react";

function Profile() {
  const [formData, setFormData] = useState({
    full_name: "",
    bio: "",
    location: "",
    availability: "",
    profile_picture: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div>
      <h1>My Profile</h1>

      <input
        type="text"
        name="full_name"
        placeholder="Full Name"
        onChange={handleChange}
      />

      <textarea
        name="bio"
        placeholder="Bio"
        onChange={handleChange}
      />

      <input
        type="text"
        name="location"
        placeholder="Location"
        onChange={handleChange}
      />

      <input
        type="text"
        name="availability"
        placeholder="Availability"
        onChange={handleChange}
      />

      <input
        type="text"
        name="profile_picture"
        placeholder="Profile Image URL"
        onChange={handleChange}
      />

      <button>Save Profile</button>
    </div>
  );
}

export default Profile;