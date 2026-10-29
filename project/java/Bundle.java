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
  A collection of Elements that have a shared context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bundle extends ElementCollection {

  private String context;


}