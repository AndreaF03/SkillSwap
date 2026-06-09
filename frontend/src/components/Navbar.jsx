import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link> |{" "}
      <Link to="/login">Login</Link> |{" "}
      <Link to="/register">Register</Link> |{" "}
      <Link to="/dashboard">Dashboard</Link> |{" "}
      <Link to="/profile">Profile</Link> |{" "}
      <Link to="/search">Search</Link> |{" "}
      <Link to="/requests">Requests</Link> |{" "}
      <Link to="/reviews">Reviews</Link>
    </nav>
  );
}

export default Navbar;