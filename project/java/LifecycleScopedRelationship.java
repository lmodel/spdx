package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Provide context for a relationship that occurs in the lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LifecycleScopedRelationship extends Relationship {

  private String scope;


}